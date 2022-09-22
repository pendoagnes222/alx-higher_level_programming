HTTP is an asymmetric request-response client-server protocol as illustrated.  An HTTP client sends a request message to an HTTP server. 
The server, in turn, returns a response message.  In other words, HTTP is a pull protocol, the client pulls information from the server 
(instead of server pushes information down to the client). 
HTTP is a stateless protocol. In other words, the current request does not know what has been done in the previous requests.
HTTP permits negotiating of data type and representation, so as to allow systems to be built independently of the data being transferred
         
              BROWSER

Whenever you issue a URL from your browser to get a web resource using HTTP, e.g.http://www.nowhere123.com/index.html, the browser turns 
the URL into a request message and sends it to the HTTP server. The HTTP server interprets the request message, and returns you an 
appropriate response message, which is either the resource you requested or an error message
