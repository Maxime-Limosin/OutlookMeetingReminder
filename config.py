import yaml

class Config:
    outlookEmail: str = ""
    outlookPassword: str = ""
    outlookServerAddress: str = ""
    synologyWebhookToken: str = ""
    
    def __init__(self, yamlFilePath: str):
        with open(yamlFilePath, 'r') as file:
            config = yaml.safe_load(file)
            
            self.outlookEmail = config['outlook']['email']
            self.outlookPassword = config['outlook']['password']
            self.outlookServerAddress = config['outlook']['serverAddress']
            self.synologyWebhookToken = config['synology']['token']
            