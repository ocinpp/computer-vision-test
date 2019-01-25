def azure_vision_test(api_key, image_url):
    """ Azure Vision test function
    
    Call Azure Cognitive API to perform the analyze;
    The image will be displayed together with the 'categories' in the JSON response
    
    Args:
        api_key: API key to be used
        image_url: Image to be passed to API for processing
        
    """
    
    header = {"Content-Type": "application/json", "Ocp-Apim-Subscription-Key": api_key}
    payload = {"url": image_url}
    
    # send to API endpoint
    r = requests.post(AZURE_API_ENDPOINT, headers=header, data=json.dumps(payload))
    
    # display the image
    display(Image(url=image_url, width=300))
    
    # print URL
    print(image_url)
    
    # load the response JSON
    jr = json.loads(r.text)

    for category in jr['categories']:
        print(category)
