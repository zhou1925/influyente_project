
from django.http import HttpResponse
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import redirect

stripe.api_key = "sk_test_51LGrjCKiBZclNpQIh3dSsvj0IL1xWchAbclzXmy630bOa2FXmoWVs9sNoCfdkWYKpY3zUeYRi4HOPExPxel2CXJp00hnaTm7T3"

@api_view(['POST'])
def create_checkout_session(request):
    """ Create checkout session """
    # create checkout Boost
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items = [{'price': price_id,'quantity': 1,}],
            mode='payment',
            success_url='http://127.0.0.1:3000/?success=true',
            cancel_url='http://127.0.0.1:3000/?canceled=true',
            payment_method_types =['card'],
        )
        print(checkout_session)
        if checkout_session != None:
            print("creating objects to null")
        #return redirect(checkout_session.url,status=303)
        return Response({"url": checkout_session.url}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': 'something went wrong try again'}, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
def webhook(request):
    """ webhook stripe """
    #endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    endpoint_secret = 'whsec_b2925248b79072fb149851d3e687299798237c00a2fef89058687b56234ea8f5' 
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session['customer_details']['email']
        # send email to celery
        send_mail("boost", "you buyed a boost", "test@gmail.com", [customer_email])
        # do something else

    return HttpResponse(status=200)
