import random
import time

class User:
    def __init__(self, resourceNeeded, timeNeeded, name):
        self.resourceNeeded = resourceNeeded
        self.timeNeeded = timeNeeded
        self.name = name

class Resource:
    def __init__(self, name):
        self.name = name
        self.userQueue = []
    def appendUserToQueue(self, user):
        self.userQueue.append(user)



numOfResources = random.randint(1,30)
#print(numOfResources)

resources = []
for num in range(0,numOfResources):
    name = 'resource'+str(num+1)
    newResource = Resource(name)
    resources.append(newResource)




numOfUsers = random.randint(1,30)

users = []
for num in range(0,numOfUsers):
    timeNeeded = random.randint(1,30)
    resourceNeeded = random.choice(resources)
    
    name = 'user'+str(num+1)
    newUser = User(resourceNeeded, timeNeeded, name)
    
    resourceNeeded.appendUserToQueue(newUser)

    users.append(newUser)


print('RESOURCES:'+'\n')
for r in resources:
    print(r.name)
    print('User Queue: ')
    if len(r.userQueue) > 0:
        for u in r.userQueue:
            print(u.name);
        print('\n')
    else:
        print('(no users in queue)'+'\n')
print('\n')


# for u in users:
#     print(u.name + ' is using ')
#     print('... ' + u.resourceNeeded.name)
#     print('for '+ str(timeNeeded)+' sec')

#display status of resources (used or idle)
#display the user using the resource & time left for user
#display the queue for resources with multiple users
#

for r in resources:
    if r.userQueue != []:
        for u in r.userQueue:
            currentUser = r.userQueue[0]
            print(r.name+' is being used by '+ currentUser.name)

            for i in range(currentUser.timeNeeded):
                if currentUser.timeNeeded > 0:
                    if len(r.userQueue) > 1:
                            print(str(currentUser.timeNeeded - i) +' sec remaining before '+r.userQueue[1].name+' can start using '+ r.name)
                            time.sleep(1)
                    elif len(r.userQueue) == 1:
                            print(str(currentUser.timeNeeded - i) +' sec remaining')
                            time.sleep(1)
                else:
                    pass
            r.userQueue.pop(0)
            #print(r.userQueue[0])
    else:
        pass