from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html> 
    <title> coding </title>
    <body> 
            <table border="2">
                   <caption> Top five Revenue Software Companies </caption>
                   <tr>
                         <th> S.No </th>
                         <td> 1 </th>
                         <td> 2 </th>
                         <td> 3 </th>
                         <td> 4 </th>
                         <td> 5 </th>
                   </tr>
                   <tr>
                         <th> company </th>
                         <td> Microsoft </th>
                         <td> Oracle </th>
                         <td> IBM </th>
                         <td> Sap </th>
                         <td> Symaantec </th>
                   </tr>
                   <tr>
                         <th> Revenue </th>
                         <td> 65 billion </td>
                         <td> 29.5 billion </td>
                         <td> 6.4 billion </td>
                         <td> 7 billion </td>
                         <td> 5 billion </td>
                   </tr>
               </table>
     </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()