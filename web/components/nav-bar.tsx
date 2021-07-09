import { Box, Stack } from "@chakra-ui/layout";
import {
  IconButton,
  Menu,
  MenuButton,
  MenuItem,
  MenuList,
  useColorMode,
} from "@chakra-ui/react";
import { HamburgerIcon, MoonIcon, SunIcon } from "@chakra-ui/icons";
import React from "react";
import NextLink from "next/link";
import UserAuthButton from "./user-auth-button";
import { Button } from "@chakra-ui/button";

interface INavBarButtonProps {
  text: string;
  href: string;
}

const navBarItems: Array<{ href: string; text: string }> = [
  {
    href: "/",
    text: "Home",
  },
  {
    href: "/authenticated",
    text: "Check auth",
  },
];
const NavBarMenuItem = (props: INavBarButtonProps) => {
  return (
    <NextLink href={props.href} passHref={true}>
      <MenuItem>{props.text}</MenuItem>
    </NextLink>
  );
};
const NavBarButton = (props: INavBarButtonProps) => {
  return (
    <NextLink href={props.href} passHref>
      <Button as="a" variant="ghost" fontWeight="400">
        {props.text}
      </Button>
    </NextLink>
  );
};
const MobileLeftNavBar = () => {
  return (
    <Box display={{ md: "none", lg: "none", xl: "none", base: "block" }}>
      <Menu>
        <MenuButton
          as={IconButton}
          aria-label="Options"
          icon={<HamburgerIcon />}
          variant="outline"
        />
        <MenuList>
          {navBarItems.map((item) => (
            <NavBarMenuItem text={item.text} href={item.href} key={item.href} />
          ))}
        </MenuList>
      </Menu>
    </Box>
  );
};
const DesktopLeftNavBar = () => {
  return (
    <Box
      flexDirection="row"
      display={{ md: "block", lg: "block", xl: "block", base: "none" }}
    >
      {navBarItems.map((item) => (
        <NavBarButton text={item.text} href={item.href} key={item.href} />
      ))}
    </Box>
  );
};
export const NavBar = () => {
  const { colorMode, toggleColorMode } = useColorMode();
  return (
    <Stack
      flexDirection="row"
      justifyContent="space-between"
      alignItems="center"
      width="100%"
      as="nav"
      p={3}
      mx="auto"
      maxW="1200px"
      wrap="wrap"
    >
      <Box flexDirection="row" mt="0.5rem">
        <IconButton
          aria-label="Toggle dark mode"
          variant="ghost"
          onClick={toggleColorMode}
          icon={colorMode == "dark" ? <SunIcon /> : <MoonIcon />}
        />
      </Box>
      <DesktopLeftNavBar />
      <MobileLeftNavBar />
      <UserAuthButton />
    </Stack>
  );
};
