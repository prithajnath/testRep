#!/usr/bin/env perl

use strict;
use warnings;

use DBI;
use DBD::SQLite;

my $dbh;



#$ENV/
sub start()
{ $dbh=DBI->connect("dbi:SQLite:/local/files/scrai002/csc341/blaise/BlaiseTracks.db",undef,undef,{AutoCommit => 1});
  die "database connect error:", $DBI::errstr unless($dbh);
}

sub stop()
{ $dbh->disconnect or die "Error disconnecting", $dbh->errstr;
}




sub ListofRuns(){

	my $sql = 'select r.rowid, r.startSecs,a.name from run as r inner join activity as a on a.categoryid=r.activityid limit 20;';
	my $sth = $dbh->prepare($sql);
	die "Prepare statement failed", $dbh->errstr unless($sth);
	my $rv=$sth->execute();
	die "Execute failed", $sth->errstr unless($rv);
	while (my @row = $sth->fetchrow_array) {
	   print "ROWID: $row[0]  START SEC: $row[1] ACTIVITY: $row[2]\n";
	}

}
#select timeMilis, latitude, longitude, altitude from tracklocation where runid=168
#select timeMilis/1000, latitude, longitude, altitude from tracklocation where runid=? and altitude is not null;
sub RunDetails($){

	my $runid = shift;
	my $sql = 'select timeMilis/1000, latitude, longitude, altitude from tracklocation where runid=?;';
	my $sth = $dbh->prepare($sql);
	die "Prepare statement failed", $dbh->errstr unless($sth);
	my $rv=$sth->execute($runid);
	die "Execute failed", $sth->errstr unless($rv);
	my $count=0;
	while (my @row = $sth->fetchrow_array) {
	   $count+=1;	
	   if (!@row[3]){
		print "$count) TIME: $row[0]  LATITUDE: $row[1] LONGITUDE: $row[2] ALTITUDE: NULL\n";}
	   else{

		print "$count) TIME: $row[0]  LATITUDE: $row[1] LONGITUDE: $row[2] ALTITUDE: $row[3]\n";

}
	}


 
}

#update run set activityid=158 where rowid=2;
sub updateRun{

	my (@activityid,@runid) = @_;
	my $runid = shift;
        my $activityid = shift;
	my $sql = 'update run set activityid=? where rowid=?';
	my $sth = $dbh->prepare($sql);
	my $rv=$sth->execute($activityid,$runid);
	die "Execute failed", $sth->errstr unless($rv);


}

#select distinct name from activity order by name;
sub activityList(){

	my $sql = 'select distinct name from activity order by name;';
	my $sth = $dbh->prepare($sql);
	$sth->execute();
	my $count=0;
	while (my @row = $sth->fetchrow_array) {
	   $count+=1;	
	   print "ACTIVITY $count) $row[0] \n";
	}



}

start;

ListofRuns();
RunDetails(147);
activityList();
#updateRun(48,87);

stop;
