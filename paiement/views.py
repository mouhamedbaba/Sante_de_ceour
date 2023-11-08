from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
import hashlib
import json
from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import Request, urlopen  
from django.views.decorators.csrf import csrf_exempt
from paiement.models import NotificationPayTech
from administration.models import DonCollect
@csrf_exempt
def paiement_view(request):
    if request.POST:
        all = request.POST
        collect_pk = None
        print('all : ', all)
        item_name = request.POST['item_name']
        if request.POST['amount'] :
            item_price = request.POST['amount']
        else :
            item_price = request.POST['fixed_amount']
        try :
            if request.POST['collect_pk']:
                collect_pk = request.POST['collect_pk']
        except :
            pass
        
        currency = "XOF"
        
        import uuid
        command_ref = str(uuid.uuid4())
        
        data = {
            "item_name": item_name,
            "item_price": item_price,
            "currency": currency,
            "ref_command": command_ref,
            "command_name": "Don",
            "ipn_url": "https://c592-41-82-64-150.ngrok-free.app/paiement/ipn",
            "env": "test"
        }

        headers = {
            "Content-Type": "application/json",
            "api_key": "fc133da925f15d32ac8f902374cf18798d9d495ad46f39b0f1f97112a5d1bb33",
            "api_secret": "cb904f3c41e8e8a3cf49deb8f9c0ecc06d44b23b9ce0754cc00eef7951ec1d8b"
        }

        url = "https://paytech.sn/api/payment/request-payment?"
        data = json.dumps(data).encode('utf-8')
        req = Request(url, data=data, headers=headers, method='POST')
        response = urlopen(req)

        if response.getcode() == 200:
            response_data = json.loads(response.read())
            success = response_data.get("success")

            if success == 1:
                if collect_pk :
                    try :
                        don = DonCollect(collect = collect_pk, amount = item_price, payement_method = "", donneur_email = request.POST['donation-email'], donneur_name = request.POST['donation-name'], confirmed = False)
                        don.save()
                    except :
                        print("don non saved")
                else :
                    print("don non reussi")
                redirect_url = response_data.get("redirect_url")
                return redirect(redirect_url)

            else:
                return HttpResponse(f"La transaction a échoué :{ response_data}")

        else:
            return HttpResponse("La requête a échoué : " + response.read(), status=response.getcode())


# Create your views here.

def sucess(request):
    return render(request, 'paiement/sucess.html')

def cancel(request):
    return render(request, 'paiement/cancel.html')

from django.http import HttpResponse
import hashlib

@csrf_exempt
def ipn(request):
    if request.POST:
        inputtxt = request.POST["getrow"]
        api_key_sha256 = request.POST["api_key_sha256"]
        api_secret_sha256 = request.POST["api_secret_sha256"]
        my_api_secret_sha256 = hashlib.sha256(b'cb904f3c41e8e8a3cf49deb8f9c0ecc06d44b23b9ce0754cc00eef7951ec1d8b').hexdigest()
        my_api_key_sha256 = hashlib.sha256(b'fc133da925f15d32ac8f902374cf18798d9d495ad46f39b0f1f97112a5d1bb33').hexdigest()

        if my_api_key_sha256 == api_key_sha256 and my_api_secret_sha256 == api_secret_sha256:
            # La requête provient de PayTech, vous pouvez traiter les informations ici.
            
            # Récupérez les paramètres de la notification IPN
            type_event = request.POST.get('type_event')
            client_phone = request.POST.get('client_phone')
            payment_method = request.POST.get('payment_method')
            item_name = request.POST.get('item_name')
            item_price = request.POST.get('item_price')
            ref_command = request.POST.get('ref_command')
            command_name = request.POST.get('command_name')
            currency = request.POST.get('currency')
            env = request.POST.get('env')
            custom_field = request.POST.get('custom_field')
            token = request.POST.get('token')
            notif = NotificationPayTech(
                type_event=type_event, client_phone=client_phone, payment_method=payment_method, item_name=item_name, item_price=item_price, ref_command=ref_command, command_name=command_name, currency=currency, env=env, custom_field=custom_field, token=token
            )
            notif.save()

            # Vérifiez le type d'événement
            if type_event == 'sale_canceled':
                # L'événement est une annulation de paiement, vous pouvez effectuer des actions spécifiques ici.
                print("Annulation de paiement détectée :")
                print(f"Type d'événement : {type_event}")
                print(f"Nom du produit : {item_name}")
                print(f"Référence de commande : {ref_command}")

            # Traitez les données comme nécessaire.

            return HttpResponse("Notification IPN traitée avec succès.")
    else:
        return HttpResponseBadRequest("Méthode non autorisée")

        
       