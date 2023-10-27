# Giving the weather information of a particular place using API (Application Programming Interface)

The basic Functionality of the API is to fetch the data required by the end user from the database. 
An API can be compared to a waiter in a restaurant who takes your order, delivers it to the chef, and then returns with the cuisine you requested. 
On the https://openweathermap.org/ , you are looking for a state's weather info, (let's say New York). You send a request (product search requested) through an API, and the database looks for the city and determines whether it is available. 
If it is available then the related information will be retrieved and returned to the end user.
If it is not available then the API will not be able to retrieve the weather information.
In such a case "City not found" will be returned. (As per the provided code)
For security reasons the OneweatherAPI will provide the API key which is unique and each and every response will be recorded.

