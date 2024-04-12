```
Prerequisites

VS Code and the Azure extensions:
Azure Account
```
**Steps**

1. Fork the repo 

2. Create a new App Service and Deploy the code to Azure:
[Quickstart: Deploy a Python web app to Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cvscode-aztools%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli)

```Azure will take care of the containerization process of our application, so no additional steps are necessary as this is one of the advantages of cloud services```

3. Once the deployment finished, navigate to the app and confirm its working:

<img width="309" alt="image" src="https://github.com/jor-gc/sre-test/assets/164224998/15fe4763-9434-4cc0-804a-188e789f78bd">

4. Once confirmed, create a testing enviroment inside the app to test changes before going to prod:[Set up staging environments in Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots?tabs=portal)

5. Add a new item in the store and deploy it to the new dev enviroment, not to prod

  <img width="352" alt="image" src="https://github.com/jor-gc/sre-test/assets/164224998/506dd3ea-5726-4a41-b240-afa24b917eab">

6. Compare both sites. notice how the new dev enviroment has a different url and shows the newly added item while prod only has 1 product

   <img width="800" alt="image" src="https://github.com/jor-gc/sre-test/assets/164224998/820857cb-aa64-45f2-9fd5-2192b049808a">

7. Now that we confirmed the change worked, we can swap enviroments using the Azure portal

   <img width="826" alt="image" src="https://github.com/jor-gc/sre-test/assets/164224998/eb929250-253b-4476-99b7-8789f64b50fe">

8. We can see the two items in prod now

    <img width="308" alt="image" src="https://github.com/jor-gc/sre-test/assets/164224998/74d57a77-59b5-4439-a6b9-c6ebf24e3d12">

### GitHub-Azure Integration

9. Push to a GitHub repo 

10. Configure the Dev enviroment to integrate with the GitHub repo

    <img width="524" alt="image" src="https://github.com/jor-gc/sre-test/assets/164224998/3a86ef69-5d69-4d21-a256-34945c24a2fb">

This will create a GitHub Actions workflow in our repository to build and deploy our app whenever there is a commit on the chosen branch

<img width="576" alt="image" src="https://github.com/jor-gc/sre-test/assets/164224998/4f6b3791-bbe2-4810-bcf3-8d26512bb38f">

11. Test the new integration by adding more items to the store

12. GitHub Actions will automatically deploy to Dev enviroment after we push to our repository

    <img width="512" alt="image" src="https://github.com/jor-gc/sre-test/assets/164224998/ce39e7c7-5bb4-46f2-9a3f-c2ecf3ee9398">

13. Deployment completed successfully

    <img width="711" alt="image" src="https://github.com/jor-gc/sre-test/assets/164224998/890a1f31-c6be-44cc-b0a0-d02c9a85df02">

14. Final result
    
    <img width="554" alt="image" src="https://github.com/jor-gc/sre-test/assets/164224998/6df26d42-98d2-48a1-808c-11cb6e1d6c98">

