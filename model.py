from network import *
from data import *
#training data
training_data = load_half_data_wrapper()
# net = load("half[44,30,17,3]withaccuracy128%")
net = Network([training_data[0][0].shape[0],30,17, training_data[0][1].shape[0]], cost=CrossEntropyCost)
a,b,c,d=net.SGD(training_data, epochs=10000, mini_batch_size=10, eta= 0.01,
            lmbda = 0.1,
            evaluation_data=None,
            monitor_evaluation_cost=False,
            monitor_evaluation_accuracy=False,
            monitor_training_cost=False,
            monitor_training_accuracy=True)         #learning rate = 0.5, number of iterations = 3000

print("Training Accuracy is:", d[-1])
# net.save("half[44,30,17,3]withaccuracy"+str(d[-1])+"%")
a=net.evaluate(training_data)
print(len(a))
# net.save("[44,30,17,3]withaccuracy"+str(d[-1])+"%")
# jpt = load("[44,30,17,3]withaccuracy172%") 

# print("Training Accuracy is:", d)
# eva = [x for (x,y) in training_data]
# print(len(eva), eva[0].shape)
# net.feedforward([x for (x,y) in training_data])
