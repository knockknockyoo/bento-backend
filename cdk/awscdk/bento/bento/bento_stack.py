from configparser import ConfigParser
from aws_cdk import core
from aws_cdk import core as cdk
from aws import iam, vpc, ecr

class BentoStack(cdk.Stack):
  def __init__(self, scope: cdk.Construct, ns: str, **kwargs) -> None:
    super().__init__(scope, ns, **kwargs)

    config = ConfigParser()
    config.read('bento.properties')
    self.config = config
    
    # VPC
    bentoVPC = vpc.VPCResources.createResources(self, ns)
    
    # IAM
    bentoIAM = iam.IAMResources.createResources(self, ns)
    
    # ECR
    bentoECR = ecr.ECRResources.createResources(self, ns)
    
    # EC2
    #bentoEC2 = ec2.EC2Resources.createResources(self, ns, config, bentoTags, bentoIAM)