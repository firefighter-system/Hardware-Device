import sys
import random
import time
import datetime
import json
import re
from pyrebase import pyrebase



config = {"apiKey": "AIzaSyA20qu9ddnRJPAQgGpn9ySQLuqjLH2WWPI",
              "authDomain": "firefightingmonitoringsystem.firebaseapp.com",
              "databaseURL": "https://firefightingmonitoringsystem.firebaseio.com/",
              "storageBucket": "firefightingmonitoringsystem.appspot.com"
             }
fireBase = pyrebase.initialize_app(config)

database = {
  "piData": {
    "users": {
      "user1": {
        "userProfile": {
          "name": "Yuji Jeong",
          "group": 10,
          "age": 23,
          "firefighterCode": "FEkdjs-23"
        },
        "status": {
          "totalMissionCount": 23,
          "currentMission": {
            "ongoingMission": True,
            "ongoingMissionNumber": 23
          }
        },
        "missionData": {
          "missionNumber": 23,
          "data": {
            "time0": {
              "timestamp": "random time sttamp",
              "userData": {
                "heartRate": 99,
                "bodyTemperature": 37.4,
                "externalTemperature": 40.0
              }
            },
            "time1": {
              "timestamp": "time stamp +5 seconds",
              "userData": {
                "heartRate": 100,
                "bodyTemperature": 37.0,
                "externalTemperature": 42.0
              }
            },
            "time2": {
              "timestamp": "time stamp +5 seconds",
              "userData": {
                "heartRate": 100,
                "bodyTemperature": 37.0,
                "externalTemperature": 42.0
              }
            }
          }
        }
      },
      "user2": {
        "userProfile": {
          "name": "Yuhan Lee",
          "group": 10,
          "age": 23,
          "firefighterCode": "FEkdjs-24"
        },
        "status": {
          "totalMissionCount": 12,
          "currentMission": {
            "ongoingMission": True,
            "ongoingMissionNumber": 23
          }
        },
        "missionData": {
          "ongoingMission": {
            "missionNumber": 23,
            "data": {
              "time0": {
                "timestamp": "random time sttamp",
                "userData": {
                  "heartRate": 99,
                  "bodyTemperature": 37.4,
                  "externalTemperature": 40.0
                }
              },
              "time1": {
                "timestamp": "time stamp +5 seconds",
                "userData": {
                  "heartRate": 100,
                  "bodyTemperature": 37.0,
                  "externalTemperature": 42.0
                }
              },
              "time2": {
                "timestamp": "time stamp +5 seconds",
                "userData": {
                  "heartRate": 100,
                  "bodyTemperature": 37.0,
                  "externalTemperature": 42.0
                }
              }
            }
          }
        }
      },
      "user3": {
        "userProfile": {
          "name": "Studio Ghibli",
          "group": 10,
          "age": 23,
          "firefighterCode": "FEkdjs-25"
        },
        "status": {
          "totalMissionCount": 23,
          "currentMission": {
            "ongoingMission": True,
            "ongoingMissionNumber": 23
          }
        },
        "missionData": {
          "ongoingMission": {
            "missionNumber": 23,
            "data": {
              "time0": {
                "timestamp": "random time sttamp",
                "userData": {
                  "heartRate": 99,
                  "bodyTemperature": 37.4,
                  "externalTemperature": 40.0
                }
              },
              "time1": {
                "timestamp": "time stamp +5 seconds",
                "userData": {
                  "heartRate": 100,
                  "bodyTemperature": 37.0,
                  "externalTemperature": 42.0
                }
              },
              "time2": {
                "timestamp": "time stamp +5 seconds",
                "userData": {
                  "heartRate": 100,
                  "bodyTemperature": 37.0,
                  "externalTemperature": 42.0
                }
              }
            }
          }
        }
      },
      "user4": {
        "userProfile": {
          "name": "Ponyo Kiki",
          "group": 10,
          "age": 23,
          "firefighterCode": "FEkdjs-26"
        },
        "status": {
          "totalMissionCount": 80,
          "currentMission": {
            "ongoingMission": True,
            "ongoingMissionNumber": 23
          }
        },
        "missionData": {
          "ongoingMission": {
            "missionNumber": 23,
            "data": {
              "time0": {
                "timestamp": "random time sttamp",
                "userData": {
                  "heartRate": 99,
                  "bodyTemperature": 37.4,
                  "externalTemperature": 40.0
                }
              },
              "time1": {
                "timestamp": "time stamp +5 seconds",
                "userData": {
                  "heartRate": 100,
                  "bodyTemperature": 37.0,
                  "externalTemperature": 42.0
                }
              },
              "time2": {
                "timestamp": "time stamp +5 seconds",
                "userData": {
                  "heartRate": 100,
                  "bodyTemperature": 37.0,
                  "externalTemperature": 42.0
                }
              }
            }
          }
        }
      },
      "user5": {
        "userProfile": {
          "name": "Eric Laroche",
          "group": 10,
          "age": 23,
          "firefighterCode": "FEkdjs-27"
        },
        "status": {
          "totalMissionCount": 3,
          "currentMission": {
            "ongoingMission": True,
            "ongoingMissionNumber": 23
          }
        },
        "missionData": {
          "ongoingMission": {
            "missionNumber": 23,
            "data": {
              "time0": {
                "timestamp": "random time sttamp",
                "userData": {
                  "heartRate": 99,
                  "bodyTemperature": 37.4,
                  "externalTemperature": 40.0
                }
              },
              "time1": {
                "timestamp": "time stamp +5 seconds",
                "userData": {
                  "heartRate": 100,
                  "bodyTemperature": 37.0,
                  "externalTemperature": 42.0
                }
              },
              "time2": {
                "timestamp": "time stamp +5 seconds",
                "userData": {
                  "heartRate": 100,
                  "bodyTemperature": 37.0,
                  "externalTemperature": 42.0
                }
              }
            }
          }
        }
      }
    }
  }
}

db = fireBase.database()
#db.set(database)



while True:
    hum1 = random.randint(30,40)
    hum2 = random.randint(30,40)
    hum3 = random.randint(30,40)
    hum4 = random.randint(30,40)

    chestTemp1 = random.randint(40,50)
    chestTemp2 = random.randint(40,50)
    chestTemp3 = random.randint(40,50)
    chestTemp4 = random.randint(40,50)

    extTemp1 = random.randint(100,120)
    extTemp2 = random.randint(100,120)
    extTemp3 = random.randint(100,120)
    extTemp4 = random.randint(100,120)

    hartbt1 = random.randint(70,100)
    hartbt2 = random.randint(70,100)
    hartbt3 = random.randint(70,100)
    hartbt4 = random.randint(70,100)


    dt = str(datetime.datetime.now().date()) + "_" + str(datetime.datetime.now().time().isoformat())
    dt = re.sub("\.", "_", dt)
    print ("Time pushed: " + dt)

    data = {
        "users":{
            "arsham":{
                "chestTemperature": chestTemp1,
                "externalTemperature": extTemp1,
                "humidity": hum1,
                "heartbeat": hartbt1,
                },
            "filip":{
                "chestTemperature": chestTemp2,
                "externalTemperature": extTemp2,
                "humidity": hum2,
                "heartbeat": hartbt2,
                },
            "franko":{
                "chestTemperature": chestTemp3,
                "externalTemperature": extTemp3,
                "humidity": hum3,
                "heartbeat": hartbt3,
                },
            "yuhan":{
                "chestTemperature": chestTemp4,
                "externalTemperature": extTemp4,
                "humidity": hum4,
                "heartbeat": hartbt4,
                },
            }
    }

    result = db.child("piData").child("users").child("user1").child("missionData").child(dt).set(data)
    print("Res: " + str(result))

    time.sleep(1)
