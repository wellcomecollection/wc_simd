#!/usr/bin/env python3
import argparse
import sys

import boto3
from botocore.exceptions import ClientError

DEFAULT_INSTANCE_ID = "i-053dc89605578305e"
DEFAULT_REGION = "eu-west-2"


def get_ec2_client(region: str):
    return boto3.client("ec2", region_name=region)


def stop_instance(client, instance_id: str):
    print(f"Stopping instance {instance_id}…")
    try:
        client.stop_instances(InstanceIds=[instance_id])
        waiter = client.get_waiter("instance_stopped")
        waiter.wait(InstanceIds=[instance_id])
        print(f"✅ Instance {instance_id} is now stopped.")
    except ClientError as e:
        print(f"Error stopping instance: {e}", file=sys.stderr)
        sys.exit(1)


def start_instance(client, instance_id: str):
    print(f"Starting instance {instance_id}…")
    try:
        client.start_instances(InstanceIds=[instance_id])
        waiter = client.get_waiter("instance_running")
        waiter.wait(InstanceIds=[instance_id])
        print(f"✅ Instance {instance_id} is now running.")
    except ClientError as e:
        print(f"Error starting instance: {e}", file=sys.stderr)
        sys.exit(1)


def parse_args():
    p = argparse.ArgumentParser(
        description="Start or stop a single EC2 instance and wait for it to change state."
    )
    p.add_argument(
        "action",
        choices=["start", "stop"],
        help="Whether to start or stop the instance",
    )
    p.add_argument(
        "--instance-id",
        default=DEFAULT_INSTANCE_ID,
        help=f"EC2 instance ID (default: {DEFAULT_INSTANCE_ID})",
    )
    p.add_argument(
        "--region",
        default=DEFAULT_REGION,
        help=f"AWS region (default: {DEFAULT_REGION})",
    )
    return p.parse_args()


def main():
    args = parse_args()
    ec2 = get_ec2_client(args.region)

    if args.action == "stop":
        stop_instance(ec2, args.instance_id)
    elif args.action == "start":
        start_instance(ec2, args.instance_id)
    else:
        # argparse should prevent this
        sys.exit("Invalid action; choose 'start' or 'stop'.")


if __name__ == "__main__":
    main()
