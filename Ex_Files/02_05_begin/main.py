import os
# os module has key env
# vars

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

# Grab OS environment variables
# if no environment name then use <DEVELOPMENT>
current_env = os.environ.get("ENV_NAME", DEVELOPMENT)
print("Current ENV IS", {current_env})

if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env in [CODE_SPACE, LOCAL]:
    print("Codespace or local environment")
else:
    print("Unknown environment")
