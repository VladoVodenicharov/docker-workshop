variable "bq_dataset_name" {
  description = "My BigQuery dataset name"
  type        = string
  default = "demo-dataset"
}

variable "gc_storage_class" {
  description = "My Google Cloud Storage class"
  type        = string
  default     = "STANDARD"
}

variable "gcs_bucket_name" {
  description = "My Google Cloud Storage bucket name"
  type        = string
  default     = "demo-bucket"
}

variable "location" {
  description = "The location of the Google Cloud Storage bucket"
  type        = string
  default     = "US"
}

variable "project" {
  description = "The project to create resources in"
  type        = string
  default     = "my-project-id" #name of the project I want to use from Google cloud
}

variable "credentials" {
  description = "my credentials"
  type        = string
  default     =  "./terraform/keys/service-account-key.json" #path to the credentials file
}

#Everything that goes as a parameter can be defined here. This is a good practice to keep the code clean and organized.
#