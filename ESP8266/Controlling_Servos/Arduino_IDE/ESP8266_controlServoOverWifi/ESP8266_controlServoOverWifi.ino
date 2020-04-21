// Mohammad Safeea - April 2020
// Wbsite:
// https://mohammadsafeea.weebly.com/

//-- Libraries Included --------------------------------------------------------------
  #include <ESP8266WiFi.h>
  #include <Servo.h>
//------------------------------------------------------------------------------------
  // Network Name and Password
  char*       net_ssid = "";              // WIFI NAME
  char*       net_pass = "";          // PASSWORD
//------------------------------------------------------------------------------------
  #define     MAXSC     6           // MAXIMUM NUMBER OF CLIENTS
  
  WiFiServer  daServer(1987);      
  WiFiClient  daClient[MAXSC];    
  Servo myservo;
  
  int servoPin=5; // IO PIN ATTACHED TO SERVO MOTOR
//====================================================================================

  void setup()
  {
    // Attaching the servo pin
    myservo.attach(servoPin);
    // Setting Serial Port
    Serial.begin(9600);           // Computer Communication

    // Setting Wifi Access Point
    SetWifi("ctrlServoOverWifi", "");
  }

//====================================================================================
  
  void loop()
  {
    // Checking For Available Clients
    AvailableClients();
    // Checking For Available Client Messages
    AvailableMessage();
  }

//====================================================================================
  
  void SetWifi(char* Name, char* Password)
  {
    // Stop Any Previous WIFI
    WiFi.disconnect();

    // Setting The Wifi Mode
    WiFi.mode(WIFI_AP_STA);
    Serial.println("WIFI Mode : AccessPoint Station");
    
    // Setting The AccessPoint Name & Password
    net_ssid      = Name;
    net_pass  = Password;
    
    // Starting The Access Point
    WiFi.softAP(net_ssid, net_pass);
    Serial.println("WIFI << " + String(net_ssid) + " >> has Started");
    
    // Wait For Few Seconds
    delay(2000);
    
    // Getting Server IP
    IPAddress IP = WiFi.softAPIP();
    
    // Printing The Server IP Address
    Serial.print("Server IP : ");
    Serial.println(IP);

    // Starting Server
    daServer.begin();
    daServer.setNoDelay(true);
    Serial.println("Server Started, you can connect from the JAVA client");
  }

//====================================================================================

  void AvailableClients()
  {   
    if (daServer.hasClient())
    {
      
     
      for(uint8_t i = 0; i < MAXSC; i++)
      {
        //find free/disconnected spot
        if (!daClient[i] || !daClient[i].connected())
        {
          // Checks If Previously The Client Is Taken
          if(daClient[i])
          {
            daClient[i].stop();
          }

          // Checks If Clients Connected To The Server
          if(daClient[i] = daServer.available())
          {
            Serial.println("New Client: " + String(i));
          }

          // Continue Scanning
          continue;
        }
      }
      
      //no free/disconnected spot so reject
      WiFiClient daClient = daServer.available();
      daClient.stop();
    }
  }

//====================================================================================

  void AvailableMessage()
  {
    //check clients for data
    for(uint8_t i = 0; i < MAXSC; i++)
    {
      if (daClient[i] && daClient[i].connected() && daClient[i].available())
      {
          while(daClient[i].available())
          {
            int angle = daClient[i].read();
            String Message = String(angle);
            Serial.println(Message);
            daClient[i].flush();           
            if(angle>-1)
            {
              if(angle<181)
              {
                myservo.write(angle);                
              }
            }
          }
      }
    }
  }

//====================================================================================
