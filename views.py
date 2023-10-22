from django.shortcuts import render
from rest_framework import viewsets
from .models import IndianState
from .serializers import IndianStateSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from requests import *

try:
	url="http://127.0.0.1:8000/indianstate"
	he = {
			"Authorization": "Token 7323338769fb8116d33dce4e58d2aea55529a569"
	}
	res = get(url, headers=he)
	print(res.status_code)
	if res.status_code == 200:
			data = res.json()
			msg = data["msg"]
			print(msg)
	else:
			print("bad credentials")
except Exception as e:
		print("issue" , e)
def home(request):
    if request.method == "POST":
        state = request.POST.get("state")
        if state == "Andhra Pradesh":
            res = "Amaravati"
            msg = "The capital is " + str(res)
        elif state == "Arunachal Pradesh":
            res = "Itanagar"
            msg = "The capital is " + str(res)
        elif state == "Assam":
            res = "Dispur"
            msg = "The capital is " + str(res)
        elif state == "Bihar":
            res = "Patna"
            msg = "The capital is " + str(res)
        elif state == "Chhattisgarh":
            res = "Raipur"
            msg = "The capital is " + str(res)
        elif state == "Goa":
            res = "Panaji"
            msg = "The capital is " + str(res)
        elif state == "Gujarat":
            res = "Gandhinagar"
            msg = "The capital is " + str(res)
        elif state == "Haryana":
            res = "Chandigarh"
            msg = "The capital is " + str(res)
        elif state == "Himachal Pradesh":
            res = "Shimla"
            msg = "The capital is " + str(res)
        elif state == "Jharkhand":
            res = "Ranchi"
            msg = "The capital is " + str(res)
        elif state == "Karnataka":
            res = "Bengaluru"
            msg = "The capital is " + str(res)
        elif state == "Kerala":
            res = "Thiruvananthapuram"
            msg = "The capital is " + str(res)
        elif state == "Madhya Pradesh":
            res = "Bhopal"
            msg = "The capital is " + str(res)
        elif state == "Maharashtra":
            res = "Mumbai"
            msg = "The capital is " + str(res)
        elif state == "Manipur":
            res = "Imphal"
            msg = "The capital is " + str(res)
        elif state == "Meghalaya":
            res = "Shillong"
            msg = "The capital is " + str(res)
        elif state == "Mizoram":
            res = "Aizawl"
            msg = "The capital is " + str(res)
        elif state == "Nagaland":
            res = "Kohima"
            msg = "The capital is " + str(res)
        elif state == "Odisha":
            res = "Bhubaneswar"
            msg = "The capital is " + str(res)
        elif state == "Punjab":
            res = "Chandigarh"
            msg = "The capital is " + str(res)
        elif state == "Rajasthan":
            res = "Jaipur"
            msg = "The capital is " + str(res)
        elif state == "Sikkim":
            res = "Gangtok"
            msg = "The capital is " + str(res)
        elif state == "Tamil Nadu":
            res = "Chennai"
            msg = "The capital is " + str(res)
        elif state == "Telangana":
            res = "Hyderabad"
            msg = "The capital is " + str(res)
        elif state == "Tripura":
            res = "Agartala"
            msg = "The capital is " + str(res)
        elif state == "Uttar Pradesh":
            res = "Lucknow"
            msg = "The capital is " + str(res)
        elif state == "Uttarakhand":
            res = "Dehradun"
            msg = "The capital is " + str(res)
        elif state == "West Bengal":
            res = "Kolkata"
            msg = "The capital is " + str(res)
        else:
            msg = "Invalid I/P"
        return render(request, "home.html", {"msg": msg})
    else:
        return render(request, "home.html")

class IndianStateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = IndianState.objects.all()
    serializer_class = IndianStateSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

			