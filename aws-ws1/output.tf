output "My_IP" {
 value = aws_instance.webos1.public_ip
}

output "My_AZ" {
 value = aws_instance.webos1.availability_zone
}

output "My_OS_Name" {
 value = aws_instance.webos1.tags
}

output "My_Server_Hard-Disk" {
  value = aws_ebs_volume.example.tags 
}

output "My_Hard-disk_attached_to"  {
    value = aws_instance.webos1.tags
}