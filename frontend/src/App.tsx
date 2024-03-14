import "./App.css"
import { Center, Grid, GridItem } from '@chakra-ui/react'
import UserInfo from "./userInfo"
import HplcHolderInfo from "./holderInfo"

export default function App() {

  return (
  <>
  <Center>
  <Grid
    h='100vh'
    w='100vw'
    gap={2}
    templateRows='repeat(2, 1fr)'
    templateColumns='repeat(5, 1fr)'
  >
    <GridItem rowSpan={2} colSpan={1}>
    <UserInfo />
    </GridItem>
    <GridItem colSpan={2} rowSpan={1}>
    <HplcHolderInfo/>
    </GridItem>
  </Grid>
  </Center>
  </>)
}