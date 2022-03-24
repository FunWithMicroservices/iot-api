while getopts h:p:e: flag
do
    case "${flag}" in
        h) ES_ENDPOINT=${OPTARG};;
        p) ES_PASSWORD=${OPTARG};;
        e) ENV=${OPTARG};;
    esac
done

export ES_ENDPOINT=$ES_ENDPOINT
export ES_PASSWORD=$ES_PASSWORD
export ENV=$ENV


# Stop Docker composition
docker-compose down

# Start Docker composition
docker-compose up -d
