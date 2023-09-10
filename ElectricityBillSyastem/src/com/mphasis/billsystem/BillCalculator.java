package com.mphasis.billsystem;

public class BillCalculator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
 int units=230;
 double billToPay=0;
 if(units<100) {
	 billToPay=units*1.20;
 }
 else if(units<300)
 {
	 billToPay=100*1.20+(units-100)*2;
 }
 System.out.println("bill for"+units+"is"+billToPay);	 
	}

}
