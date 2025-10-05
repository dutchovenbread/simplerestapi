"""
Simple REST API application
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handler for simple REST API requests"""
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                'status': 'ok',
                'message': 'Simple REST API is running',
                'timestamp': datetime.now().isoformat(),
                'endpoints': {
                    '/': 'API status and available endpoints',
                    '/health': 'Health check endpoint'
                }
            }
            self.wfile.write(json.dumps(response, indent=2).encode())
            logger.info('GET / - 200 OK')
            
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                'status': 'healthy',
                'timestamp': datetime.now().isoformat()
            }
            self.wfile.write(json.dumps(response, indent=2).encode())
            logger.info('GET /health - 200 OK')
            
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                'status': 'error',
                'message': 'Endpoint not found',
                'timestamp': datetime.now().isoformat()
            }
            self.wfile.write(json.dumps(response, indent=2).encode())
            logger.warning(f'GET {self.path} - 404 Not Found')
    
    def log_message(self, format, *args):
        """Override to suppress default logging"""
        pass


def run_server(host='0.0.0.0', port=8080):
    """Start the HTTP server"""
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    logger.info(f'Starting server on {host}:{port}')
    print(f'Server running on http://{host}:{port}')
    print('Press Ctrl+C to stop')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info('Server stopped by user')
        print('\nServer stopped')


if __name__ == '__main__':
    run_server()
