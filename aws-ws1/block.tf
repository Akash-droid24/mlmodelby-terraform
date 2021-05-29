resource "aws_ebs_volume" "example" {
  availability_zone = aws_instance.webos1.availability_zone
  size              = 1

  tags = {
    Name = "My Volume"
  }
}
