import "./App.css"
import {  HStack } from '@chakra-ui/react'
import UserInfo from "./userInfo"
import HolderInfo from "./holderInfo"
import {HplcSampleInfo, BatchSampleInfo}from "./sampleInfo"
import BufferInfo from "./bufferInfo"

export default function App() {
  return (
  <>
    <HStack>
      <UserInfo/>
      <HolderInfo/>
      <HplcSampleInfo/>
      <BatchSampleInfo/>
      <BufferInfo/>
    </HStack>
  </>)
}