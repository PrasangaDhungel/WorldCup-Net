import network
import predictdata

# load
net = network.load("model.h5")

print("""Teams are:  argentina colombia  egypt     iceland   morocco        poland        senegal   australia   
         costa-rica  england   iran      nigeria   portugal  serbia         switzerland   sweden
         belgium     croatia   france    japan     panama    russia         south-korea   tunisia 
         brazil      denmark   germany   mexico    peru      saudi-arabia   spain         uruguay 
    """)

home_team = input("Enter a home team:  ")
away_team = input("Enter a away team:  ")


test_data1 = predictdata.get_test_data(home_team, away_team)
test_data2 = predictdata.get_test_data(away_team, home_team)
a = net.evaluate(test_data1)
b = net.evaluate(test_data2)
if(a[0] == 1 or (a[0]==b[0])):
    print("Result is Draw")
elif(a[0] == 0):
    print(away_team + " will win")
else:
    print(home_team + " will win")
