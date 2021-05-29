resource "aws_instance" "webos1" {
  ami           = "ami-010aff33ed5991201"
  instance_type = "t2.micro"
  security_groups =  [ "TeraSG" ]
  key_name = "terraform_key"
  availability_zone = "ap-south-1a"

  tags = {
    Name = "ML OS"
  }

}