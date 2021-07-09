import React, { ReactNode } from "react";
import Head from "next/head";
import { Flex, Stack } from "@chakra-ui/layout";
import { NextSeo } from "next-seo";
import { NavBar } from "./nav-bar";

type LayoutProps = {
  children?: ReactNode;
  title: string;
  description?: string;
};

const Layout = ({ children, title, description }: LayoutProps) => {
  return (
    <>
      <NextSeo
        title={title}
        description={description}
        openGraph={{
          title: title,
          description: description,
        }}
      />
      <div>
        <Head>
          <title>{title}</title>
          <meta charSet="utf-8" />
          <meta
            name="viewport"
            content="initial-scale=1.0, width=device-width"
          />
          <link rel="icon" type="image/png" href="/static/logo.png" />
        </Head>
        <header>
          <NavBar />
        </header>
        <Flex
          as="main"
          justifyContent="center"
          flexDirection="column"
          px={4}
          mx="auto"
          mt={8}
          maxW="1000px"
        >
          <Stack spacing={10}>{children}</Stack>
        </Flex>
      </div>
    </>
  );
};

export default Layout;
