## Run uvicorn server locally

1. Start uvicoen server on reload mode
```uvicorn main:app --reload  ```
You can also use the thunder client but the swagger has considerably more options for interaction as compared to the other two,.
Can fetch the users from the db using the unique customer Id and based on their conversations we can be able to pass the to the ML api endpoint and retreive a response. 
2. There is an interactive documentation provided by swagger. TO access the documetation we can be able to use the ```http://127.0.0.1:8000/docs```
The socumentation woerks in the same way as the python script itself for sending items. 
I need to get the documents from the db and immediately pass them to the model that I would have stored and hosted on the docker compute platfform
3. There is another documentation known as the api readdoc but it is not interactive as compared to the other ones.