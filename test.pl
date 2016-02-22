#!/usr/bin/perl
use strict;
use warnings;
use 5.010;

print "\nPress 1 for Farhenheit to Celsius conversion\nPress 2 for Celsius to Farhenheit conversion\nPress 3 to exit\n ";
my $num = <STDIN>;

my $val = 0;
my $conv = 0;
if ($num == 1) {
	print 'Enter temp in Farenheit : ';
	$val = <STDIN>;
	$conv = (5/9)*($val-32);
	print "Celsius: $conv\n";
}

elsif ($num == 2) {
	print 'Enter temp in Celsius : ';
	$val = <STDIN>;
	$conv = (9/5)*$val+32;
	print "Farhenheit: $conv\n";
}

elsif ($num == 3) {
	exit;
}

else{
	print "\nError! Run the program again"; 

}





