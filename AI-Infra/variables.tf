variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "ai-translator"
}

variable "vpc_cidr" {
  description = "VPC CIDR"
  type        = string
  default     = "10.0.0.0/16"
}

variable "ecr_repository_name" {
  description = "ECR repository name"
  type        = string
  default     = "ai-translator-app"
}

variable "alert_email" {
  description = "Email address for CloudWatch alerts"
  type        = string
}