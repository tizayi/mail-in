import "./App.css"
import {  HStack } from '@chakra-ui/react'
import UserInfo from "./userInfo"
import HplcHolderInfo from "./holderInfo"

export default function App() {
  return (
  <>
    <HStack>
      <UserInfo/>
      <HplcHolderInfo/>
    </HStack>
  </>)
}