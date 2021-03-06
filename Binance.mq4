//+------------------------------------------------------------------+
//|                                                           EA.mq4 |
//|                                                                  |
//|                                                                  |
//+------------------------------------------------------------------+
#property copyright ""
#property link      ""

extern int magicnumber, ticket;
int SL, TP;
   string cookie=NULL,headers;
string symbol, typeop;
string order[];
   char post[],result[];
int res;
string url="http://127.0.0.1:80/home";
string geturl="http://127.0.0.1:80/home";
double timeout = 500;
double open, close, profit, quantity;

//+------------------------------------------------------------------+
//| expert initialization function                                   |
//+------------------------------------------------------------------+


//+------------------------------------------------------------------+
//| expert start function                                            |
//+------------------------------------------------------------------+
int filehandle;


int OnInit()
{
   return(INIT_SUCCEEDED);
}
 
void OnDeinit(const int reason)
{
 
}

bool start()
  {

  
  }
  
 
  
bool ScanIstruction(){

   res=WebRequest("POST",geturl,cookie,NULL,timeout,post,0,result,headers);

  if (res!=-1){
  int filehandle=FileOpen("answer.txt",FILE_WRITE|FILE_TXT);
      //--- Checking errors
      if(filehandle!=INVALID_HANDLE)
        {
         //--- Save the contents of the result[] array to a file
         FileWriteArray(filehandle,result,0,ArraySize(result));
         //--- Close the file
         FileClose(filehandle);
        }
      else Print("Error in FileOpen. Error code=",GetLastError());
     }
  else
  return(false);
  
}  

bool getSignals(){
   
   
filehandle= FileOpen("SignalInfo.csv",FILE_WRITE|FILE_CSV);
   FileWrite( filehandle,"TimeCurrent", "SignalID","Signalpips","Signalsubscr","Signalname","Signalcurrency");
   
   for (int i= 0; i<SignalBaseTotal(); i++){
      
      string segnale = SignalBaseSelect(i);
      
      if(segnale==TRUE)
        {
         //--- get signal properties
         long   id    =SignalBaseGetInteger(SIGNAL_BASE_ID);          // signal id
         long   pips  =SignalBaseGetInteger(SIGNAL_BASE_PIPS);        // profit in pips
         long   subscr=SignalBaseGetInteger(SIGNAL_BASE_SUBSCRIBERS); // number of subscribers
         string name  =SignalBaseGetString(SIGNAL_BASE_NAME);         // signal name
         double price =SignalBaseGetDouble(SIGNAL_BASE_PRICE);        // signal price
         string curr  =SignalBaseGetString(SIGNAL_BASE_CURRENCY);     // signal currency
         //--- print all profitable free signals with subscribers
         if(price==0.0 && pips>0 && subscr>0)
            PrintFormat("id=%d, name=\"%s\", currency=%s, pips=%d, subscribers=%d, price=%d",id,name,curr,pips,subscr);
        }
      else PrintFormat("Error in call of SignalBaseSelect. Error code=%d",GetLastError());
    
   
     if(filehandle!=-1)
       {
      FileSeek(filehandle,0,SEEK_CUR);
      FileWrite(filehandle,TimeCurrent(), id,pips,subscr,name,curr);
      
       }
      else Print("Operation FileOpen failed, error ",GetLastError());  
   }
  FileClose(filehandle);
 
   }


//+------------------------------------------------------------------+
//| Posting a message with an image on the wall at mql5.com          |
//+------------------------------------------------------------------+

bool openOrder(){

         
   filehandle= FileOpen("WriteOrder.csv",FILE_READ|FILE_CSV);
   string symbol = FileReadString(filehandle);
   string volume= FileReadString(filehandle);
  // string tipo= FileReadString(filehandle);
     int tipo=0;
   string sl= FileReadString(filehandle);
   string tp= FileReadString(filehandle);
   Print(symbol+""+volume+""+tipo+""+sl+""+tp);
   
  
   double price=Ask;
  
   double vol = StrToDouble(volume);
   //--- calculated SL and TP prices must be normalized
   double stoploss= StrToDouble(sl);
   double takeprofit= StrToDouble(tp);

//--- place market order to buy 1 lot
   int ticket=OrderSend(symbol,tipo,vol,price,3,stoploss,takeprofit,"My order",16384,0,clrGreen);
   if(ticket<0)
     {
      Print("OrderSend failed with error #",GetLastError());
     }
   else
      Print("OrderSend placed successfully");
             
         FileClose(filehandle);
      
}  

bool info(){

         
   filehandle= FileOpen("MarketInfo.csv",FILE_WRITE|FILE_CSV);
   FileWrite(filehandle,"TimeCurrent", "Symbol","Price");
   
   for (int i = 0; i<SymbolsTotal(TRUE); i++){
      
      string simbolo = SymbolName(i,TRUE);
      
      Print(simbolo + ""+MarketInfo(simbolo,MODE_BID));
    
     if(filehandle!=-1)
       {
      FileSeek(filehandle,0,SEEK_CUR);
      FileWrite(filehandle,TimeCurrent(), simbolo,MarketInfo(simbolo,MODE_BID));
      
       }
      else Print("Operation FileOpen failed, error ",GetLastError());  
 
   }
 
         FileClose(filehandle);
}  

bool infoAccount(){

         
   filehandle= FileOpen("InfoConto.csv",FILE_WRITE|FILE_CSV);
   FileWrite(filehandle,TimeCurrent(),"AccountBalance", "AccountName","AccountNumber");
   
      float balance = AccountBalance();
      string name = AccountName();
      string id = AccountNumber();

      
      Print(balance + "" + name + " "+id);
    
     if(filehandle!=-1)
       {
      FileSeek(filehandle,0,SEEK_CUR);
      FileWrite(filehandle,TimeCurrent(), balance, name ,id);
      
       }
      else Print("Operation FileOpen failed, error ",GetLastError());  
 
   
         FileClose(filehandle);
}  


bool checkUpdate(){
filehandle= FileOpen("Update.csv",FILE_READ|FILE_CSV);
 string code = FileReadString(filehandle);
 float sl = FileReadString(filehandle);
  float tp = FileReadString(filehandle);
   printf(code);
   
   FileClose(filehandle);
   
   OrderSelect(code,SELECT_BY_TICKET);
  
   float lots = OrderLots();
   string type = OrderType();
 
   if(type==1)
   type=Ask;
   else
   type=Bid;
   
   if(sl==-1&&tp==-1){
   OrderClose(code,lots,type,3);
   }
   else if (sl==-2&&tp==-2){
   SignalSubscribe(code);
   }
   else{
    OrderModify(code,OrderOpenPrice(),sl,tp,0);
     printf(tp);
   }
   
 

}


bool CheckOpenOrders(){
   //We need to scan all the open and pending orders to see if there is there is any
   //OrdersTotal return the total number of market and pending orders
   //What we do is scan all orders and check if they are of the same symbol of the one where the EA is running
       printf(OrdersTotal());
      
 filehandle= FileOpen("Register.csv",FILE_WRITE|FILE_CSV);
 FileWrite(filehandle,"TimeCurrent", "Ticket","TipoOP","Simbolo","Apertura",
            "StopLoss","TakeProfit","Chiusura", "Quantità", "Profitto");
      
  FileSeek(filehandle,0,SEEK_CUR);
  
   for( int i = 0 ; i < OrdersTotal() ; i++ ) {
     
         //We select the order of index i selecting by position and from the pool of market/pending trades
      OrderSelect( i, SELECT_BY_POS, MODE_TRADES );
      //If the pair of the order (OrderSymbol() is equal to the pair where the EA is running (Symbol()) then return true
               
            ticket = OrderTicket();
            typeop = OrderType();
            symbol = OrderSymbol();
            open = OrderOpenPrice();
            SL = OrderStopLoss();
            TP = OrderTakeProfit();
            close = OrderClosePrice();
            quantity = OrderLots();
            profit = OrderProfit();
          
            PrintFormat("Ticket: "+ticket+ " Tipo: " +typeop + " Simbolo: " +symbol+
            " Prezzo Apertura: " + open + " PrezzoChiusura: " +close + " SL: "+SL+ " TP: "+TP + " quantity: " + quantity + " profit: " + profit);  
             
           if(filehandle!=INVALID_HANDLE)
            {
             FileSeek(filehandle,0,SEEK_CUR);
            FileWrite(filehandle,TimeCurrent(), ticket,typeop,symbol,open,SL,TP,close,quantity,profit);
      
            }
            else Print("Operation FileOpen failed, error ",GetLastError());  

   }
   
       FileClose(filehandle);
            Print("FileOpen OK");
            res=WebRequest("GET",url,cookie,NULL,timeout,post,0,result,headers);
         Print(res);
   //If the loop finishes it mean there were no open orders for that pair
     return(true);
     
}
 
 
void OnTick()
{
   //getSignals();
   info();
   CheckOpenOrders();
   infoAccount();
   checkUpdate();
   //ScanIstruction();
  

  
}  