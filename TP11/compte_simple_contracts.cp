// CTD11 SVL 2015-2016 - TP contracts + interp abstraite - M. Nebut
// Compte sans découvert

using System;
using System.Diagnostics.Contracts;

class Account {
  public int balance; // marche pas avec float
                     // si pas public pas accessible dans spec
  public bool overdraft_authorized;
  public int overdraft_amount;
  
  [ContractInvariantMethod]
   void ObjectInvariant () {
       Contract.Invariant(balance >= 0); 
   }
   
  public Account() {
    Contract.Ensures(balance == 0);
     
       balance = 0;
     }

  public void credit(int amount) {
    Contract.Requires(amount>0);
    Contract.Ensures(balance == Contract.OldValue(balance) + amount) ;

    balance += amount;
  } 
     
  public void debit(int amount) { 
    Contract.Requires(amount <= balance); 
    Contract.Ensures(balance == Contract.OldValue(balance) - amount);
    
      balance -= amount;
    }
}

