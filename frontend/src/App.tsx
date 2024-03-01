import "./App.css"
import {  HStack } from '@chakra-ui/react'
import UserInfo from "./user"
import { HolderInfo } from "./holder"

export default function App() {
  return (
<>
<HStack>
<UserInfo/>
<HolderInfo/>
</HStack>
</>)
}