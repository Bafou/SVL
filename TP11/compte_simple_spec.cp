// CTD11 SVL 2015-2016 - TP spec# - M. Nebut
// Compte sans découvert

class Account {
  public int balance; // marche pas avec float
                      // si pas public pas accessible dans spec

  public Account()
    ensures balance == 0;
     {
       balance = 0;
     }

  public void credit(int amount)
    requires amount>0;
    ensures balance == old(balance) + amount ;
  {
    balance += amount;
  } 
     
  public void debit(int amount)
    requires amount <= balance;
    ensures balance == old(balance) - amount;
    {
      balance -= amount;
    }
}
