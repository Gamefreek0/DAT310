function BankAccount(name, balance){

this.name = name;
this.balance = balance;

this.deposit = function deposit(amount){
  this.balance = this.balance + amount;
}

this.withdraw = function withdraw(amount){
  if (amount<this.balance) {
    this.balance = this.balance - amount;
  }
  else {
    console.log("Insufficient funds! Only " + this.balance + " available, withdrawal ignored.");
  }
}

}
