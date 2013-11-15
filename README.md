Introduction to Hadoop and MapReduce
=====

## Part II

MapReduce Queries for an anonymized Web server log file

```
The logfile is in Common Log Format:

10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

%h %l %u %t \"%r\" %>s %b

Where:

%h is the IP address of the client
%l is identity of the client, or "-" if it's unavailable
%u is username of the client, or "-" if it's unavailable
%t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
%r is the request line from the client is given (in double quotes). 
   It contains the method, path, query-string, and protocol or the request.
%>s is the status code that the server sends back to the client.
%b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.
```

1) return number of hits for each different file on the Web site<br>
2) return number of hits to the site made by each different IP address<br>
3) return most popular file on the Web site (full path + number of hits)<br>



