# Mini project - LSTM stock price prediction 
This is a mini project to make a long short term memory (LSTM) recurrent neural network (RNN). This project is based off a tutorial linked below in the references section.

*Note:* This is an unfinished project, it was abandoned due to other schoolwork commitments, and when I returned to it I realised that the tesla dataset I was using does not have uniformily distriobuted data in time, making it unsuitable for use with this beginners project.

## Libraries Required:
- keras
- tensorflow
- numpy 
- pandas

## Function
Running the main.py script will create a RNN and train it on a dataset of Teslas stock opening prices between 2010 and 2018. The model is then tested against data from 2018 to 2020.
The predicted opening stock prices are compared to the real stock prices in a plot that is shown below, it is clear that the model is not a perfect fit, but broadly follows the same pricing trends as the real data. 


### References:
https://www.simplilearn.com/tutorials/deep-learning-tutorial/rnn#:~:text=Long%20Short%2DTerm%20Memory%20Networks,modules%20of%20a%20neural%20network.
