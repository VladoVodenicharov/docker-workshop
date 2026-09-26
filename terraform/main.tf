terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "8.4.0"
    }
  }
}

provider "google" {
  project = "my-project-id"
  region  = "eu-central"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "terraform-demo-bucket"
  location      = "US"
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

