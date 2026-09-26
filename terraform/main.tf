terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "8.4.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials) #path to the credentials file
  project = var.project  #project name goes here (service)
  region  = "eu-central"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = var.gcs_bucket_name #name of the bucket you want to create
  location      = var.location #location of the bucket you want to create
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3  #days
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "demo-dataset" {
  dataset_id                  = var.bq_dataset_name #put the name of the dataset you want to create
}
