# IS-4990-eventmanager-project
My project is an event manager project that allows users to keep track of events they want to attend and will allow them to edit or delete any events they have created. I am working to deploy my project to Azure in app service and utilize Azure Active Directory to allow for users to login via a Microsoft account.

### Azure diagram
![image describing Azure services intended for use](./images/LucidchartAzDiagram.png)

### Project DFD

![image of project DFD](./images/DFD.png)

### The Services Used
I used Azure App Service to deploy my app to Azure and a PostgreSQL database since the base database for django is a sqlite database which is not able to be imported to Azure. I also use the Azure Active Directory and a B2C tenant to allow for users to login to my app securely.

### Adherence to the 5 pillars of the Azure Well Architected Framework


### Future Revisions
