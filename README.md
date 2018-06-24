# Bank-loan-defaulter-prediction-system-using-statistical-logistic-regression

Bank Loan defaulter Predictor is a system designed to remove Bad debts from Bank loan Provision. Bad Debts are normally due to disbursement of loans to customer who look good on paper, or the loan evaluation officer misses out on certain flags and hence passes the loan. By using Statistical Logistic Regression trained to determine these bad debts on past data with financial and non financial input vectors, we can reject potential bad customers or flag and monitor already provisioned high risk loans so that bad debts can be predicted in advance and hence do not get converted into Non Performing Assets. 

Python modules are deployed on Django app to develop a full fledged system for Bank Official.



### Setup:
- Open the folder

- Open terminal and run the following commands :

sudo chmod 755 run.sh
sudo chmod 755 setup.sh

- Then 

bash setup.sh or ./setup.sh

This may take a few minutes..

### Usage:
Type the following in the terminal

source bin/activate
bash run.sh

**After a few moments the server will start and you can see the link in your terminal. Open the link in your browser and use the application

1. On starting, you'll see a login page. Type username 'sangat' and password 'sangat4119' and login to the application

2. Once logged in you will see 3 icons. Clicc on the prediction icon.

3. On clicking on the prediction icon, you'll be redirected to a form where you can enter the details of the customer. On clicking the predict button an alert will be displayed stating the results.

4. Once finished, go to the dashboard and click on logout icon and log out of the application.
