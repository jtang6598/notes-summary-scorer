from lambda_function import lambda_handler


if __name__ == '__main__':
    event = {
        'files': ['documents/Positive Pysch - Can Money Buy Happiness_.docx'],
        'notes': None,
        'summary': 'Money can buy you happiness, as long as you spend it on the right things. There was a study conducted in a mall, with different types of purchases that showed that.'
    }
    # event = {'resource': '/evaluate', 'path': '/evaluate', 'httpMethod': 'POST', 'headers': {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-us', 'content-type': 'multipart/form-data', 'Host': 'mkvr98xejc.execute-api.us-east-2.amazonaws.com', 'origin': 'http://localhost:3000', 'referer': 'http://localhost:3000/', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15', 'X-Amzn-Trace-Id': 'Root=1-604db212-7ff482a036c011723012a174', 'X-Forwarded-For': '174.74.8.144', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'accept': ['*/*'], 'accept-encoding': ['gzip, deflate, br'], 'accept-language': ['en-us'], 'content-type': ['multipart/form-data'], 'Host': ['mkvr98xejc.execute-api.us-east-2.amazonaws.com'], 'origin': ['http://localhost:3000'], 'referer': ['http://localhost:3000/'], 'User-Agent': ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'], 'X-Amzn-Trace-Id': ['Root=1-604db212-7ff482a036c011723012a174'], 'X-Forwarded-For': ['174.74.8.144'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': 'd0t7sk', 'resourcePath': '/evaluate', 'httpMethod': 'POST', 'extendedRequestId': 'cKjC7EGWCYcFldQ=', 'requestTime': '14/Mar/2021:06:49:54 +0000', 'path': '/test/evaluate', 'accountId': '361415370669', 'protocol': 'HTTP/1.1', 'stage': 'test', 'domainPrefix': 'mkvr98xejc', 'requestTimeEpoch': 1615704594651, 'requestId': 'e67e5df8-2064-46b7-b273-0ed0b83c8e73', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'sourceIp': '174.74.8.144', 'principalOrgId': None, 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15', 'user': None}, 'domainName': 'mkvr98xejc.execute-api.us-east-2.amazonaws.com', 'apiId': 'mkvr98xejc'}, 'body': '------WebKitFormBoundaryhkPBzaCCH5WTm3qe\r\nContent-Disposition: form-data; name="files"; filename="testDocx.docx"\r\nContent-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document\r\n\r\n\r\n------WebKitFormBoundaryhkPBzaCCH5WTm3qe\r\nContent-Disposition: form-data; name="notes"\r\n\r\nffr\r\n------WebKitFormBoundaryhkPBzaCCH5WTm3qe\r\nContent-Disposition: form-data; name="summary"\r\n\r\ngggg\r\n------WebKitFormBoundaryhkPBzaCCH5WTm3qe--\r\n', 'isBase64Encoded': False}
    print(lambda_handler(event, None))
