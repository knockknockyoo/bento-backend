import os
from configparser import ConfigParser
from aws_cdk import core
from aws_cdk import core as cdk
from aws import iam, vpc, ecr, ecsCluster, ecsService, alb, albListener, ec2, route53


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

    # ECS Cluster
    bentoECSCluster = ecsCluster.ECSCluster.createResources(self, ns)

    # ALB
    bentoALB = alb.ALBResources.createResources(self, ns)    

    # ECS Services
    bentoECSService = ecsService.ECSService.createResources(self, ns)

    # ALB Listener
    bentoALBListener = albListener.ALBListener.createResources(self, ns)    

    # EC2
    bentoEC2 = ec2.EC2Resources.createResources(self, ns)

    # Route53
    bentoDNS = route53.Route53Resources.createResources(self, ns)

    # Outputs
    cdk.CfnOutput(self, "Database-IP",
        value=self.DBInstance.instance_private_ip,
        description="The IP address assigned to the DB Instance",
        export_name="dbipaddress")