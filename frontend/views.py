from django.shortcuts import render
import requests
import json

# Create your views here.
API_URL = "http://127.0.0.1:8000/api/v1/"

def test(request):
    return render(request, "index.html")

def acara(request):
    url = API_URL + "acara/"
    response = requests.get(url)

    if response.status_code == 200:
        api_data = response.json()  # Convert response to JSON
        print(api_data)
        context = {
            'api_data': api_data,
        }
        return render(request, 'all_acara.html', context)
    return render(request, "all_acara.html")

def api_call(request):
    if request.method == 'GET':
        return render(request, "api_call.html")
    
    elif request.method == 'POST':
        method=request.POST.get('method')
        path = request.POST.get('path')
        url = API_URL + path
        
        if method == "GET":
        

            try:

                response = requests.get(url)

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Extract the JSON data from the response
                    print(response.json())
                    context={
                        'res': response.json()
                    }
                    return render(request, "response.html", context)
                else:
                    # If the request was not successful, return an error response
                    return render(request, "response.html", context={'res':'Failed to call the external API'})

            except requests.exceptions.RequestException as e:

                return render(request, "response.html", context={'res':'Failed to call the external API'})
            
        if method == "POST":

            body = request.POST.get('body')
            json_object = json.loads(body)

            try:
                # Make a POST request to the external API
                response = requests.post(url, json=json_object)
                print(response)

                # Check if the request was successful (status code 200)
                if response.status_code == 201:
                    # Extract the JSON data from the response
                    context={
                        'res':response.json()
                    }
                    return render(request, "response.html", context)
                else:
                    # If the request was not successful, return an error response
                    return render(request, "response.html", context={'res':'Failed to call the external API'})
            except requests.exceptions.RequestException as e:
                # If an exception occurs during the request, return an error response
                return render(request, "response.html", context={'res':'Failed to call the external API'})
                
        if method == "DELETE":
            try:
                # Make a DELETE request to the external API
                response = requests.delete(url)

                # Check if the request was successful (status code 204 for successful DELETE)
                if response.status_code == 204:
                    return render(request, "response.html", context={'res':'Resource deleted successfully'})
                else:
                    # If the request was not successful, return an error response
                    return render(request, "response.html", context={'res':'Failed to call the external API'})
            except requests.exceptions.RequestException as e:
                # If an exception occurs during the request, return an error response
                return render(request, "response.html", context={'res':'Failed to call the external API'})

        if method == "PUT":
            body = request.POST.get('body')
            json_object = json.loads(body)

            try:
                # Make a POST request to the external API
                response = requests.put(url, json=json_object)
                print(response)

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Extract the JSON data from the response
                    context={
                        'res':response.json()
                    }
                    return render(request, "response.html", context)
                else:
                    # If the request was not successful, return an error response
                    return render(request, "response.html", context={'res':'Failed to call the external API'})
            except requests.exceptions.RequestException as e:
                # If an exception occurs during the request, return an error response
                return render(request, "response.html", context={'res':'Failed to call the external API'})
            
def api_list(request):
    return render(request, "api_list.html")