#!/usr/bin/env perl

use strict;
use warnings;

use DBI;
use DBD::SQLite;

my $dbh;


sub start()
{ $dbh=DBI->connect("dbi:SQLite:$ENV{HOME}/files/csc341/blaise/BlaiseTracks.db",undef,undef,{AutoCommit => 1});
  die "database connect error:", $DBI::errstr unless($dbh);
}
  
sub getLatestRun($)
{ my $activity=shift;

  my $sth=$dbh->prepare_cached(q{
    select max(r.ROWID) as ROWID
      from run as r
      inner join activity as a on r.activityid=a.ROWID and a.name=?}, undef, 3);
  die "Prepare statement failed", $dbh->errstr unless($sth);

  my $rv=$sth->execute($activity);
  die "Execute failed", $sth->errstr unless($rv);

  my $runid;
  
  do
  { while(my $aref=$sth->fetchrow_arrayref)
    { 
      $runid=$aref->[0];
    }
    die "Fetch failed", $sth->errstr if($sth->err);
  } while($sth->more_results);
  $sth->finish;
  return $runid;
}

sub printTracks($)
{ my $runid=shift;

  my $sth=$dbh->prepare_cached(q{
    select timeMilis, latitude, longitude, altitude
      from tracklocation where runid=?}, undef, 3);
  die "Prepare statement failed", $dbh->errstr unless($sth);

  my $rv=$sth->execute($runid);
  die "Execute failed", $sth->errstr unless($rv);

  my $runid;

  do
  { while(my $aref=$sth->fetchrow_arrayref)
    { print @$aref,"\n";
    }
    die "Fetch failed", $sth->errstr if($sth->err);
  } while($sth->more_results);

  $sth->finish;
}

sub printRun
{ 

	my ($rowid, $startSecs, $name);
	my $sth = $dbh -> prepare("
	select r.ROWID, r.startSecs, a.name
      		from run as r
      		inner join activity as a on a.categoryid=r.activityid"
	);
	$sth->execute();
	$sth->bind_col(1, \$rowid);
	$sth->bind_col(2, \$startSecs);
	$sth->bind_col(3, \$name);
	while($sth->fetch){print "$rowid $startSecs $name\n";}

}



sub stop()
{ $dbh->disconnect or die "Error disconnecting", $dbh->errstr;
}

start;
print "getting the runid of the latest run\n";
my $runid=getLatestRun("walk");
print "The latest snowshoe run is $runid\n";
print "Printing the tracks based on row id now\n";
printTracks($runid);
print "Now printing the runs!\n";
printRun;
stop();
