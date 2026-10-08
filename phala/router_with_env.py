"""Measured launcher: deliver existing backend token without secret CLI arguments."""
import os
import sys
from vllm_router.launch_router import launch_router, parse_router_args

args = parse_router_args(sys.argv[1:])
token = os.environ.get('TOKEN')
if not token:
    raise SystemExit('Existing unified TOKEN is required')
args.api_key = token
launch_router(args)
