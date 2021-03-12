package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"os"

	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/eks"
)

const (
	Version    = "dev"
	Source     = "https://github.com/njgibbon/sek"
	ConfigPath = ".sek.yaml"
)

func main() {
	flag.Parse()
	if flag.Arg(0) == "version" {
		fmt.Println(Version)
		os.Exit(0)
	}
	if flag.Arg(0) == "doc" || flag.Arg(0) == "help" {
		fmt.Println(Source)
		os.Exit(0)
	}
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		log.Fatal(err)
	}

	client := eks.NewFromConfig(cfg)
	output, err := client.ListClusters(context.TODO(), &eks.ListClustersInput{})
	if err != nil {
		log.Fatal(err)
	}

	log.Println(output)
	log.Println(output.Clusters)
}
