# Walking HashiCorp Configuration Language (HCL) structure recursively while marking resources, modules, and dependencies
import hcl2

def walk_hcl(data, indent=0):
    spacing = ' ' * indent # Note the use of single space for indentation in HCL
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "resource":
                print(f"{spacing}{key} (Resource):")
            elif key == "module":
                print(f"{spacing}{key} (Module):")
            elif key == "depends_on":
                print(f"{spacing}{key} (Dependency):")
            else:
                print(f"{spacing}{key}:")
            walk_hcl(value, indent + 1)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            print(f"{spacing}[{index}]:")
            walk_hcl(item, indent + 1)
    else:
        print(f"{spacing}{data}")

# Example HCL data
hcl_data = '''
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro" 
  depends_on = [aws_security_group.sg]
}
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  version = "2.77.0"
}
'''

data = hcl2.loads(hcl_data)  # Parse HCL string into Python data structure
walk_hcl(data)  # Walk through and print the HCL structure