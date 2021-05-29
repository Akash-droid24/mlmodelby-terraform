
resource "null_resource"  "nullremote1" {

depends_on = [
  aws_volume_attachment.ebs_att
]

connection {
    type     = "ssh"
    user     = "ec2-user"
    private_key = file("C:/Users/Akash/Downloads/terraform_key.pem")
    host     = aws_instance.webos1.public_ip
  }

provisioner "remote-exec" {
    inline = [
      "sudo yum  install docker  -y",
      "sudo systemctl start docker",
      "sudo systemctl enable docker",
      "sudo docker info",
      "sudo docker ps",
      "sudo docker images",
      "sudo docker pull centos",
      "sudo docker run -it --name mymlos1 centos",

    ]
  }

}